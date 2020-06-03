import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CreateComponent as EventCreateComponent } from './events/create/create.component';
import { ListComponent as EventListComponent } from './events/list/list.component';


const routes: Routes = [
  {
    path: 'create',
    component: EventCreateComponent,
  },
  {
    path: '',
    component: EventListComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
