import { Component, Input } from '@angular/core';
import { Tag } from '../../modules/interfaces';

@Component({
  selector: 'app-tag-details',
  templateUrl: './tag-details.component.html',
  styleUrls: ['./tag-details.component.scss']
})
export class TagDetailsComponent {
  @Input() tag!: Tag;
}
