import redis from 'redis';
import kue from 'kue';

const client = redis.createClient();

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '123456789',
  message: 'this is a message'
}).save();

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});


job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (errorMessage) => {
  console.log(`Notification job failed: ${errorMessage}`);
});
