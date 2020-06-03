import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { ApiService } from '../api.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  loginForm = this.fb.group({
    email: [null, Validators.required],
    password: [null, Validators.required]
  });
  isLoadingResults = false;
  hide = true;

  constructor(private fb: FormBuilder, private api: ApiService, private router: Router) {}

  onSubmit() {
    this.isLoadingResults = true;
    this.api.login(this.loginForm.value)
      .subscribe((res: any) => {
        console.log(res);
      }, (err: any) => {
        console.log(err);
      });
    this.isLoadingResults = false;
  }
}
