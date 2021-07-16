import React from "react";
import {shallow, ShallowWrapper} from "enzyme";
import SignUp from "../SignUp";

describe("component ...", () => {
    let component: ShallowWrapper;

    const setUp = (props?: any) => shallow(<SignUp {...props}/>)

    beforeEach(() => {
        component = setUp();
    });

    test("component should render", () => {
        expect(component).toMatchSnapshot();
    });

    test("component ", () => {
        const mockedFunc = jest.fn();
        let component = shallow(<SignUp />);
        // don't know how to mock func and pass it to component and test it call times
        expect(mockedFunc).toBeCalledTimes(1);
    });
});
