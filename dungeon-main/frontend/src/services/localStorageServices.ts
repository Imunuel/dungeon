interface Storage {
    key: string,
    value: any
}

export const saveToStorage = ({key, value}: Storage): void => {
    window.localStorage.setItem(key, value);
}

export const getFromStorage = (key: string): string | null => {
    return window.localStorage.getItem(key);
}