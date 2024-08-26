import kue from 'kue';
import redis from 'redis';

// Create a Redis client
const redisClient = redis.createClient();

// Create a Kue queue
const queue = kue.createQueue();

// Define the sendNotification function
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Process jobs from the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  
  // Call the sendNotification function with the job data
  sendNotification(phoneNumber, message);
  
  // Mark the job as complete
  done();
});

// Handle job completion
queue.on('job complete', (id) => {
  console.log(`Job ${id} completed`);
});

// Handle job failure
queue.on('job failed', (id, errorMessage) => {
  console.log(`Job ${id} failed: ${errorMessage}`);
});
