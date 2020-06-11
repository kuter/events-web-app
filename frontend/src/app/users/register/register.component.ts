import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { ApiService } from '../api.service';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  registerForm = this.fb.group({
    email: [null, Validators.required],
    password: [null, Validators.required],
    passwordRepeat: [null, Validators.required]
  });
  isLoadingResults = false;
  data = {};
  hide = true;

  private prepareRequest(form) {
    return {
      email: form.value.email,
      password: form.value.password,
      password2: form.value.passwordRepeat
    };
  }

  constructor(private fb: FormBuilder, private api: ApiService, private router: Router) {}

  onSubmit() {
    this.isLoadingResults = true;
    this.data = this.prepareRequest(this.registerForm);
    console.log(this.data);
    this.api.register(this.data)
      .subscribe((res: any) => {
        console.log(res);
        this.router.navigate(['login']);
      }, (err: any) => {
        console.log(err);
      });
    this.isLoadingResults = false;
  }
}
