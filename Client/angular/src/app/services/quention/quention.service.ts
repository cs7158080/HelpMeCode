import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Question } from '../../modules/interfaces';

@Injectable({
  providedIn: 'root'
})
export class QuentionService {

  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  createQuention(quention: Question): Observable<Question> {
    return this.http.post<Question>(`${this.apiUrl}/questions/createQuention`, quention);
  }

  getAllQuentions(): Observable<Question[]> {
    return this.http.get<Question[]>(`${this.apiUrl}/questions/getAllQuentions`);
  }

  getLastQuention(): Observable<Question> {
    return this.http.get<Question>(`${this.apiUrl}/questions/getLastQuention`);
  }

  getQuentionsByTags(tags: string): Observable<Question[]> {
    return this.http.get<Question[]>(`${this.apiUrl}/questions/getQuentionsByTags/${tags}`);
  }
}
