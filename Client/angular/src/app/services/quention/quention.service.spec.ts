import { TestBed } from '@angular/core/testing';

import { QuentionService } from './quention.service';

describe('QuentionService', () => {
  let service: QuentionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(QuentionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
