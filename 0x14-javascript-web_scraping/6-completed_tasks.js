#!/usr/bin/node
const request = require('request');

const url = process.argv[2] + '?completed=true';
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);
  const taskDict = {};
  for (const task of tasks) {
    if (task.userId in taskDict) {
      taskDict[task.userId]++;
    } else {
      taskDict[task.userId] = 1;
    }
  }
  console.log(taskDict);
});
