import { Component, OnInit } from '@angular/core';
import { PostService } from '../../services/post/post.service'; 
import { Post } from '../../modules/interfaces';
import { CommonModule } from '@angular/common';
import { PostDetailsComponent } from '../post-details/post-details.component';

@Component({
  selector: 'app-post',
  imports: [CommonModule,PostDetailsComponent],
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {
  posts: Post[] = [];

  constructor(private postService: PostService) { }

  ngOnInit(): void {
    this.loadPosts();
  }

  loadPosts(): void {
    this.postService.getAllPosts().subscribe((data: Post[]) => {
      this.posts = data;
    });
  }
}