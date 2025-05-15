import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tag } from '../../modules/interface';
@Injectable({
  providedIn: 'root'
})
export class TagService {
   private baseUrl = 'http://localhost:8000'

    constructor(private http: HttpClient) { }

    getAlltags(): Observable<Array<Tag>>{
        return this.http.get<Array<Tag>>(`${this.baseUrl}/tags/getAllTags`)        
    }
}
