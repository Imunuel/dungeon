import {Method} from "axios";
import {useCallback, useState} from "react";
import axinstance from "../utils/axios";


const useFetch = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const request = useCallback(async (url: string, method: Method, data?: Object) => {
        try {
            setLoading(true);
            const response = await axinstance.request({
                method: method,
                url: url,
                data: data
            })
            switch (response.status) {
                case 201:
                    setLoading(false);
                    return response;
                case 400:
                    setLoading(false);
                    setError("400");
                    return null;
            }
            return response
        } catch (err) {
            setError(err.message);
        }
    }, []);

    return {request, loading, error}
}

export default useFetch;