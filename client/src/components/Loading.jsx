import React from "react";
import { usePromiseTracker } from "react-promise-tracker";
import {ThreeDots} from 'react-loader-spinner';

function Loading() {
    const { promiseInProgress } = usePromiseTracker();
    return  (
        promiseInProgress &&
            <div
              style={{
                width: "100%",
                height: "100",
                display: "flex",
                justifyContent: "center",
                alignItems: "center"
              }}
            >
            <ThreeDots color="rgba(135,155,255,1)" height="100" width="100" />
            </div>
    );
}

export default Loading;