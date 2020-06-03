import { Component, OnInit } from '@angular/core';

import { ApiService } from '../api.service';


@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.scss']
})
export class LogoutComponent implements OnInit {

  constructor(private api: ApiService) { }

  ngOnInit(): void {
    this.api.logout();
  }

}
