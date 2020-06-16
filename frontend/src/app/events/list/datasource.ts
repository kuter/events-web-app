import { HttpClient } from '@angular/common/http';
import { merge, Observable, of as observableOf} from 'rxjs';

import { environment } from '../../../environments/environment';

import { Event } from '../interfaces';


const apiUrl = environment.apiUrl;

export class EventDataSource {

  constructor(private client: HttpClient) {}

  getEvents(sort: string, order: string, page: number, size: number): Observable<Event[]> {
    const requestUrl = `${apiUrl}/api/events/`;

    return this.client.get<Event[]>(requestUrl);
  }
}
