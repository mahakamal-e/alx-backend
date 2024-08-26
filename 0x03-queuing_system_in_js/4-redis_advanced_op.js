import redis from 'redis';

const client = redis.createClient();

const schools = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

for (const [key, value] of Object.entries(schools)) {
  client.hset('HolbertonSchools', key, value, redis.print);
}

client.hgetall('HolbertonSchools', (error, reply) => {
  if (error) console.error(error);
  else console.log(reply);
});
