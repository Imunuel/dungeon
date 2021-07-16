interface ILocation {
    EU: string,
    AS: string,
    NA: string,
    SA: string,
    AF: string,
    OC: string,
    [key: string]: string;
}

export const LOCATIONS: ILocation = {
    EU: "Europe",
    AS: "Asia",
    NA: "North America",
    SA: "South and Central America",
    AF: "Africa",
    OC: "Australia and Oceania",
}
