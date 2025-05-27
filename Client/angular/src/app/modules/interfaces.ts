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

export interface Question {
    Date: string;
    Context: string;
    Tags: number[];
    UserId: string;
}

export interface Content {
    context: string;
    userName: string;
}

export interface Post {
    Date: string;
    label: string;
    Context: string;
    Tags: number[];
    UserId: string;
    Content: Content[];
}

export interface Answer {
    Date: string;
    Context: string;
    Tags: number[];
    UserName: string;
    Content: Content[];
    QuestionId: string;
}
