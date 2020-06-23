import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent {
  eventForm = this.fb.group({
    title: [null, Validators.required],
    description: [null, Validators.required],
    date: [null, Validators.required],
  });
  isLoading = false;

  constructor(private fb: FormBuilder, private api: ApiService) {}

  onSubmit() {
    this.isLoading = true;
    console.log(this.eventForm.value);
    this.api.createMovie(this.eventForm.value)
      .subscribe((res: any) => {
        console.log(res);
      }, (err: any) => {
        console.log(`err: ${err}`);
      });
    this.isLoading = false;
  }
}
