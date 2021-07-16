export enum AuthActions {
    AUTHENTICATE = "AUTHENTICATE",
    AUTH_SET_LOG_IN = "AUTH_SET_LOG_IN",
    AUTH_SET_ERROR = "AUTH_SET_ERROR"
}

export type AuthState = {
    isLogged: boolean,
}
