import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../../modules/interfaces';

@Injectable({
  providedIn: 'root'
})

export class UserService {
  private apiUrl = 'http://localhost:8000'; 

  constructor(private http: HttpClient) { }

  getAllUsers(): Observable<User[]> {
    return this.http.get<User[]>(`${this.apiUrl}/users/getall`);
  }

  getUsersByName(username: string): Observable<User> {
  return this.http.get<User>(`${this.apiUrl}/users/getuserbyname/${username}`);
}

getUsersByTags(tags: string[]): Observable<User[]> {
  const params = { tags };
  return this.http.get<User[]>(`${this.apiUrl}/users/getusersbytags/`, { params });
}

  getUsersByTagsTrue(tags: string[]): Observable<User[]> {
    const params = { tags };
    return this.http.get<User[]>(`${this.apiUrl}/users/getusersbytagstrue/`, { params });
  }

  getUsersByTagsFalse(tags: string[]): Observable<User[]> {
    const params = { tags };
    return this.http.get<User[]>(`${this.apiUrl}/users/getusersbytagsfalse/`, { params });
  }
 

}