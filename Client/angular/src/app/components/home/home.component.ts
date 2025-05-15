import { Component, ChangeDetectorRef, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, ValidationErrors } from '@angular/forms';
import { Tag } from '../../modules/interface';
import { TagService } from '../../services/tag/tag.service';
import { CommonModule } from '@angular/common'; // הוספת CommonModule
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  imports: [CommonModule],
  styleUrls: ['./home.component.scss'] // תוקן מ-styleUrl ל-styleUrls
})
export class HomeComponent implements OnInit {

  myForm: FormGroup;
  alltags: Tag[] = []; // הוספת משתנה לאחסון הטאגים

  constructor(private tagService: TagService, private cdr: ChangeDetectorRef) {
    this.myForm = new FormGroup({
      tagname: new FormControl('', [Validators.required, Validators.pattern('[A-Za-zא-ת .]*')])
    });
  }

  ngOnInit() {
    this.getall();
    this.cdr.detectChanges();
  }

  // save() {
  //   if (this.myForm.valid) {
  //     const { controls } = this.myForm;
  //     let tag: Tag = {
  //       tagname: controls['tagname'].value
  //     };
  //     // כאן תוכל להוסיף קוד לשמור את הטאג
  //   }
  // }

getall() {
  this.tagService.getAlltags().subscribe(
    data => 
      this.alltags = data
  );
}



  getControlErrors(controlName: string): ValidationErrors | null {
    return this.myForm.controls[controlName].errors;
  }
}
