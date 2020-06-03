import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { Observable, of, throwError } from 'rxjs';
import { catchError, tap, map } from 'rxjs/operators';

import { environment } from '../environments/environment';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};
const apiUrl = environment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  constructor(private http: HttpClient) { }

  getMovies(): Observable<object[]> {
    console.log(apiUrl);
    return this.http.get<object[]>(apiUrl)
    .pipe(
      map(posts => posts),
        tap(posts => console.log('fetched movies')),
        catchError(this.handleError('getMovies', []))
    );
  }

  createMovie(movie: object) {
    return this.http.post<object>(apiUrl, movie, httpOptions).pipe(
      tap((c: object) => console.log(c)),
      catchError(this.handleError<object>('createMovie'))
    );
  }

}
