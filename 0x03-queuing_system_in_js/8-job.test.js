import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  it('should throw an error if jobs is not an array', () => {
    const queue = kue.createQueue();
    expect(() => {
      createPushNotificationsJobs('not an array', queue);
    }).to.throw(Error, 'Jobs is not an array');
  });

  it('should create a job for each job object in the array', () => {
    const queue = kue.createQueue();
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);

    queue.process('push_notification_code_3', (job, done) => {
      try {
        expect(job.data).to.include({
          phoneNumber: job.data.phoneNumber,
          message: job.data.message
        });
        done();
      } catch (error) {
        done(error);
      }
    });
  });
});
