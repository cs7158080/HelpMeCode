import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Post } from '../../modules/interfaces'; 

@Injectable({
  providedIn: 'root'
})
export class PostService {

  private apiUrl = 'http://localhost:8000'; 

  constructor(private http: HttpClient) { }

  createPost(post: Post): Observable<Post> {
    return this.http.post<Post>(`${this.apiUrl}/posts/createPost`, post);
  }

  getAllPosts(): Observable<Post[]> {
    return this.http.get<Post[]>(`${this.apiUrl}/posts/getAllposts`);
  }

  getLastPost(): Observable<Post> {
    return this.http.get<Post>(`${this.apiUrl}/posts/getLastPost`);
  }

  getPostsByTags(tags: string): Observable<Post[]> {
    return this.http.get<Post[]>(`${this.apiUrl}/posts/getPostsByTags/${tags}`);
  }
}