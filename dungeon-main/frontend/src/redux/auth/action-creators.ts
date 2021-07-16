import {AuthActions} from "./types";
import {AuthActionType} from "./actions";
import {Dispatch} from "redux";


export const setLogged = (isLogged: boolean) => {
    return (dispatch: Dispatch<AuthActionType>) => {

        dispatch({
            type: AuthActions.AUTH_SET_LOG_IN,
            payload: isLogged
        })
    }
}