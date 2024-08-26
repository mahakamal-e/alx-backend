import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

// Promisify Redis client methods
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Define async function for setting a new school
const setNewSchool = async (schoolName, value) => {
  try {
    const reply = await setAsync(schoolName, value);
    console.log(`Reply: ${reply}`);
  } catch (err) {
    console.error(`Error setting school: ${err}`);
  }
}

// Define async function for displaying school value
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error getting school value: ${err}`);
  }
}

// Define an async wrapper function to execute the operations
const run = async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

// Call the async wrapper function
run();
