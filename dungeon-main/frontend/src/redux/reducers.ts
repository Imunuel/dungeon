import { combineReducers } from "redux";
import {authReducer} from "./auth/reducers";

export const reducers = combineReducers({
    auth: authReducer
})

export type State = ReturnType<typeof reducers>
