import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { catchError, tap, map, shareReplay } from 'rxjs/operators';

import { environment } from '../../environments/environment';

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
};
const apiUrl = environment.apiUrl;

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }


  // Login
  login(credentials: object) {
    console.log(credentials);
    const url = `${apiUrl}/api/token/`;
    return this.http.post<object>(url, credentials, httpOptions).pipe(
      tap((c: object) => this.setSession(c)),
      catchError(this.handleError<object>('login'))
    );
  }

  private setSession(authResult) {
    localStorage.setItem('jwt_access', authResult.access);
    localStorage.setItem('jwt_refresh', authResult.refresh);
  }

  // Logout
  logout() {
    console.log('logout called');
    localStorage.removeItem('jwt_access');
    localStorage.removeItem('jwt_refresh');
  }

  // Register
  register(data: object) {
    console.log(data);
    const url = `${apiUrl}/api/register/`;
    return this.http.post<object>(url, data, httpOptions).pipe(
      tap((c: object) => console.log(c)),
      catchError(this.handleError<object>('register'))
    );
  }

}
