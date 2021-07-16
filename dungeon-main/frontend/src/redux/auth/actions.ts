import {AuthActions} from "./types";


export type AuthActionAuthenticate = {
    type: AuthActions.AUTHENTICATE
}

export type AuthActionLogIn = {
    type: AuthActions.AUTH_SET_LOG_IN
    payload: boolean
}

export type AuthActionSetError = {
    type: AuthActions.AUTH_SET_ERROR,
    payload: {}
}

export type AuthActionType = AuthActionAuthenticate | AuthActionLogIn | AuthActionSetError
