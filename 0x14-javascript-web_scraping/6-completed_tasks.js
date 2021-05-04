#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);
  const taskDict = {};
  for (const task of tasks) {
    if (task.completed) {
      const id = task.userId;
      taskDict[id] = (taskDict[id] + 1 || 1);
    }
  }
  console.log(taskDict);
});
