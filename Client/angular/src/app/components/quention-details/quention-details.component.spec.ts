import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuentionDetailsComponent } from './quention-details.component';

describe('QuentionDetailsComponent', () => {
  let component: QuentionDetailsComponent;
  let fixture: ComponentFixture<QuentionDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QuentionDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QuentionDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
