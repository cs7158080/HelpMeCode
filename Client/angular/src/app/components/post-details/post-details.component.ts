import { Component, Input } from '@angular/core';
import { Post } from '../../modules/interfaces';

@Component({
  selector: 'app-post-details',
  templateUrl: './post-details.component.html',
  styleUrls: ['./post-details.component.scss']
})
export class PostDetailsComponent {
  @Input() post!: Post;
}
