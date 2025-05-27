import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tag } from '../../modules/interfaces'; 

@Injectable({
  providedIn: 'root'
})
export class TagService {

  private apiUrl = 'http://localhost:8000'; 

  constructor(private http: HttpClient) { }

  getAllTags(): Observable<Tag[]> {
    return this.http.get<Tag[]>(`${this.apiUrl}/tags/getalltags`);
  }

  getTagsByName(tagname: string): Observable<Tag[]> {
    return this.http.get<Tag[]>(`${this.apiUrl}/tags/get-tags-by-name/${tagname}`);
  }

  createTag(tag: Tag): Observable<Tag> {
    return this.http.post<Tag>(`${this.apiUrl}/tags/create-tags`, tag);
  }
}
