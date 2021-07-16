import React, {useState} from "react";
import {Box, Button, CircularProgress, MenuItem, Popover, Select, TextField, Typography} from "@material-ui/core";
import {LOCATIONS} from "./constants";
import {useForm, Controller, SubmitHandler} from "react-hook-form";
import useFetch from "../../hooks/useFetch";
import {Alert} from "@material-ui/lab"

type Inputs = {
    username: string,
    password: string,
    location: string,
    email: string
}

const defaultValues = {
    username: "",
    password: "",
    location: "",
    email: ""
}

const rePattern = new RegExp("^[a-zA-Z0-9]+$");


const SignUp: React.FC = () => {
    const {control, handleSubmit, formState: {errors}} = useForm<Inputs>({defaultValues})
    const [anchor, setAnchor] = useState<HTMLElement | null>(null);
    const [popoverState, setPopoverState] = useState("");
    const {request, loading, error} = useFetch();
    const open = Boolean(anchor);

    const handleClose = (): void => {
        setAnchor(null);
    }

    const submitHandler: SubmitHandler<Inputs> = async (data, event) => {
        const response = await request("/api/v1/users/create/", "POST", {...data});
        switch (response?.status) {
            case 201:
                setPopoverState("Created!")
                break;
            case 400:
                setPopoverState(error);
                break;
        }
        setAnchor(event?.target)
    };

    return (
        <>
            <Box display="flex" justifyContent="center">
                <Box>
                    <form onSubmit={handleSubmit(submitHandler)}>
                        <Controller
                            render={({field}) => (
                                <TextField
                                    {...field}
                                    label="username"/>
                            )}
                            name="username"
                            defaultValue=""
                            rules={{
                                required: true,
                                pattern: rePattern
                            }}
                            control={control}/>
                        {
                            errors.username && <Alert severity="error">Username must be alphanumeric sequence!</Alert>
                        }
                        <Controller
                            render={({field}) => (
                                <TextField
                                    type="password"
                                    {...field}
                                    label="password"/>
                            )}
                            defaultValue=""
                            control={control}
                            rules={{
                                required: true,
                                pattern: rePattern
                            }}
                            name="password"/>
                        {
                            errors.password && <Alert severity="error">Password must be alphanumeric sequence!</Alert>
                        }
                        <Controller
                            control={control}
                            defaultValue=""
                            rules={{
                                required: true
                            }}
                            render={({field}) => (
                                <TextField
                                    {...field}
                                    type="email"
                                    label="email"/>)
                            }
                            name="email"/>
                        {
                            errors.email && <Alert severity="error">Email field is required!</Alert>
                        }
                        <Controller
                            control={control}
                            rules={{
                                required: true,
                            }}
                            render={({field}) => (
                                <Select
                                    {...field}
                                    label="location">
                                    {
                                        Object.keys(LOCATIONS).map((code) => {
                                            return <MenuItem key={code} value={code}>{LOCATIONS[code]}</MenuItem>
                                        })
                                    }
                                </Select>
                            )}
                            name="location"/>
                        {
                            errors.location && <Alert severity="error">Location field is required!</Alert>
                        }
                        <Button type="submit" variant="contained">{loading ? <CircularProgress/> : "Submit"}</Button>
                    </form>
                </Box>
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
                <Typography>{popoverState}</Typography>
            </Popover>
        </>
    )
}

export default SignUp;