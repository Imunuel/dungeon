import React, {useEffect} from 'react';
import {useDispatch, useSelector} from "react-redux";
import {BrowserRouter as Router, Redirect, Route, Switch} from "react-router-dom";
import {CircularProgress} from "@material-ui/core";
import {State} from "./redux/reducers";
import {getFromStorage} from "./services/localStorageServices";
import axinstance from "./utils/axios";
import {bindActionCreators} from "redux";
import * as authActionCreators from "./redux/auth/action-creators";


const SignUp = React.lazy(() => import("./components/SignUp"));
const Auth = React.lazy(() => import("./components/Auth"));
const Navigation = React.lazy(() => import("./components/Navigation"));


function App() {
    const dispatch = useDispatch();
    const {setLogged} = bindActionCreators(authActionCreators, dispatch)

    useEffect(() => {
        const token = getFromStorage("token");
        if (token) {
            axinstance.defaults.headers["Authorization"] = `Token ${token}`;
            setLogged(true);
        }
    }, [])
    const state = useSelector((state: State) => state);

    return (
        <Router>
            <React.Suspense fallback={<div className="progress-init"><CircularProgress size={100}/></div>}>
                <Switch>
                    <Route exact path="/" component={Navigation}/>
                    <Route path="/signup" component={SignUp}/>
                    <Route path="/auth">
                        {state.auth.isLogged ? <Redirect to="/"/> : <Auth/>}
                    </Route>
                </Switch>
            </React.Suspense>
        </Router>
    );
}

export default App;
