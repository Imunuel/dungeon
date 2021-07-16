import React, {useCallback, useEffect, useState} from "react";
import {saveToStorage} from "../../services/localStorageServices";
import {Box, Button, CircularProgress, Popover, TextField, Typography} from "@material-ui/core";
import {useDispatch, useSelector} from "react-redux";
import {bindActionCreators} from "redux";
import * as authActionCreators from "../../redux/auth/action-creators";
import {State} from "../../redux/reducers";
import {Controller, SubmitHandler, useForm} from "react-hook-form";
import useFetch from "../../hooks/useFetch";
import {Alert} from "@material-ui/lab";


type AuthFormInputs = {
    username: string,
    password: string
}

const defaultValues: AuthFormInputs = {
    username: "",
    password: ""
}

const Auth: React.FC = () => {
    const [anchor, setAnchor] = useState<HTMLFormElement | null>(null);
    const [popoverMessage, setPopoverMessage] = useState("");
    const {control, handleSubmit, formState: {errors}} = useForm<AuthFormInputs>({defaultValues})
    const {request, error, loading} = useFetch();
    const open = Boolean(anchor);

    const dispatch = useDispatch();
    const {setLogged} = bindActionCreators(authActionCreators, dispatch);
    const state = useSelector((state: State) => state.auth)

    const handleClose = (): void => {
        setAnchor(null);
    };

    const submitHandler: SubmitHandler<AuthFormInputs> = useCallback(async (data, event) => {
        const response = await request("/auth/", "POST", {...data});
        switch (response?.status) {
            case 200:
                setLogged(true);
                saveToStorage({key: "token", value: response?.data["token"]})
                break;
            case 403 || 404 || 400:
                setAnchor(event?.target)
                break;
        }
    }, [setLogged, request]);


    useEffect(() => {
        setPopoverMessage(error)
    }, [error])

    return (
        <>
            <Box display="flex" justifyContent="center">
                <Box>
                    <form onSubmit={handleSubmit(submitHandler)}>
                        <Controller
                            render={({field}) => (
                                <TextField
                                    label="username"
                                    {...field}/>
                            )}
                            rules={{
                                required: true
                            }}
                            name="username"
                            control={control}/>
                        {
                            errors.username && <Alert severity="error">Username is required!</Alert>
                        }
                        <Controller
                            control={control}
                            render={({field}) => (
                                <TextField
                                    type="password"
                                    {...field}
                                    label="password"/>
                            )}
                            name="password"/>
                        {
                            errors.password && <Alert severity="error">Password is required!</Alert>
                        }
                        <Button type="submit" variant="contained">{loading ? <CircularProgress/> : "Submit"}</Button>
                    </form>
                </Box>
                <Popover
                    open={open}
                    anchorEl={anchor}
                    onClose={handleClose}
                    anchorOrigin={{
                        vertical: 'bottom',
                        horizontal: 'left',
                    }}
                    transformOrigin={{
                        vertical: 'top',
                        horizontal: 'left',
                    }}>
                    <Typography>
                        {popoverMessage}
                    </Typography>
                </Popover>
            </Box>
        </>
    )
}

export default Auth;