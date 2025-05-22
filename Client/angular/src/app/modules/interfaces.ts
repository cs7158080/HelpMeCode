

export interface Tag {
    tagname: string;
}

export interface UserTag {
    tag: Tag;
    canhelp: boolean;
}

export interface User {
    name: string;
    email: string; 
    tags: UserTag[];
}
