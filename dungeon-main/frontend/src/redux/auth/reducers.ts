import {AuthActionType} from "./actions";
import {AuthActions, AuthState} from "./types";


const defaultState: AuthState = {
    isLogged: false,
}

export const authReducer = (state: AuthState = defaultState, action: AuthActionType) => {
    switch(action.type) {
        case AuthActions.AUTH_SET_LOG_IN:
            return {
                ...state,
                isLogged: action.payload
            }
        case AuthActions.AUTH_SET_ERROR:
            return {
                ...state,
                error: action.payload
            }
        default:
            return state
    }
}