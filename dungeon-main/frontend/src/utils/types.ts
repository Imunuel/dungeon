export type Credentials = {
    username: string,
    password: string,
}

export interface Profile extends Credentials {
    location: string
    email: string
}