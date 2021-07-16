import {Link} from "react-router-dom";
import React, {useState} from "react";
import {
    Drawer,
    IconButton,
    List,
    ListItem,
    ListItemIcon,
    ListItemText,
    Toolbar,
    Typography
} from "@material-ui/core";
import MenuIcon from "@material-ui/icons/Menu";
import {ExitToApp, PersonAdd} from "@material-ui/icons";


interface ListItemLinkProps {
    icon?: React.ReactElement;
    primary?: string;
    to: string;
}


const ListItemLink: React.FC<ListItemLinkProps> = ({icon, primary, to}) => {
    return (
        <li>
            <ListItem component={Link} to={to}>
                {icon ? <ListItemIcon>{icon}</ListItemIcon> : null}
                <ListItemText><Typography variant="button">{primary || ""}</Typography> </ListItemText>
            </ListItem>
        </li>
    );
}


const Navigation = () => {
    const [toggle, setToggle] = useState(false);

    const toggleDrawer = ():void => {
        setToggle(Boolean(Number(toggle) ^ 1));
    };

    return (
        <>
            <Toolbar>
                <IconButton
                    onClick={toggleDrawer}
                    edge="start">
                    <MenuIcon/>
                </IconButton>
            </Toolbar>
            <Drawer
                open={toggle}
                anchor="left"
                onClose={toggleDrawer}>
                <List>
                    <ListItemLink to="/signup" icon={<ExitToApp/>}/>
                    <ListItemLink to="/auth" icon={<PersonAdd/>}/>
                </List>
            </Drawer>

        </>
    )
}

export default Navigation;
