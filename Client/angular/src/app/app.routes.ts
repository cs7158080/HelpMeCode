import { Routes } from '@angular/router';
import { UserComponent } from './components/user/user.component';
import { TagComponent } from './components/tag/tag.component';
import { QuentionComponent } from './components/quention/quention.component';
import { PostComponent } from './components/post/post.component';
import { AnswerComponent } from './components/answer/answer.component';

export const routes: Routes = [
    { path: '', component: UserComponent } ,
    { path: 'tag', component: TagComponent } ,
    { path: 'quention', component: QuentionComponent } ,
    { path: 'post', component: PostComponent } ,
    { path: 'answer', component: AnswerComponent } 

];
