import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuentionComponent } from './quention.component';

describe('QuentionComponent', () => {
  let component: QuentionComponent;
  let fixture: ComponentFixture<QuentionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QuentionComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QuentionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
