const { spawn } = require('child_process');

const child1 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_0-60.py"]);
const child2 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_60-120.py"]);
const child3 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_120-180.py"]);
const child4 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_180-240.py"]);
const child5 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_240-300.py"]);
const child6 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_300-360.py"]);
const child7 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_360-420.py"]);
const child8 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_420-480.py"]);
const child9 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_480-540.py"]);
const child10 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_540-600.py"]);
const child11 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_600-660.py"]);
const child12 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_660-720.py"]);
const child13 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_720-780.py"]);
const child14 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_780-840.py"]);
const child15 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_840-900.py"]);
const child16 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_900-960.py"]);
const child17 = spawn('python3', ["./simulation-scripts/random-round1/simulation_random_960-1001.py"]);


child1.stdout.on('data', (data)=> {
    console.log(`simulation_random_0-60.py: \n${data}`)
});
child1.stderr.on('data', (data)=> {
    console.log(`simulation_random_0-60.py: \n${data}`)
});
child1.on('close', (code) => {
    console.log(`simulation_random_0-60.py exited with code ${code}`);
})

child2.stdout.on('data', (data)=> {
    console.log(`simulation_random_60-120.py: \n${data}`)
});
child2.stderr.on('data', (data)=> {
    console.log(`simulation_random_60-120.py: \n${data}`)
});
child2.on('close', (code) => {
    console.log(`simulation_random_60-120.py exited with code ${code}`);
})

child3.stdout.on('data', (data)=> {
    console.log(`simulation_random_120-180.py: \n${data}`)
});
child3.stderr.on('data', (data)=> {
    console.log(`simulation_random_120-180.py: \n${data}`)
});
child3.on('close', (code) => {
    console.log(`simulation_random_120-180.py exited with code ${code}`);
})

child4.stdout.on('data', (data)=> {
    console.log(`simulation_random_180-240.py: \n${data}`)
});
child4.stderr.on('data', (data)=> {
    console.log(`simulation_random_180-240.py: \n${data}`)
});
child4.on('close', (code) => {
    console.log(`simulation_random_180-240.py exited with code ${code}`);
})

child5.stdout.on('data', (data)=> {
   console.log(`simulation_random_240-300.py: \n${data}`)
});
child5.stderr.on('data', (data)=> {
   console.log(`simulation_random_240-300.py: \n${data}`)
});
child5.on('close', (code) => {
   console.log(`simulation_random_240-300.py exited with code ${code}`);
})

child6.stdout.on('data', (data)=> {
   console.log(`simulation_random_300-360.py: \n${data}`)
});
child6.stderr.on('data', (data)=> {
   console.log(`simulation_random_300-360.py: \n${data}`)
});
child6.on('close', (code) => {
   console.log(`simulation_random_300-360.py exited with code ${code}`);
})

child7.stdout.on('data', (data)=> {
   console.log(`simulation_random_360-420.py: \n${data}`)
});
child7.stderr.on('data', (data)=> {
   console.log(`simulation_random_360-420.py: \n${data}`)
});
child7.on('close', (code) => {
   console.log(`simulation_random_360-420.py exited with code ${code}`);
})

child8.stdout.on('data', (data)=> {
   console.log(`simulation_random_420-480.py: \n${data}`)
});
child8.stderr.on('data', (data)=> {
   console.log(`simulation_random_420-480.py: \n${data}`)
});
child8.on('close', (code) => {
   console.log(`simulation_random_420-480.py exited with code ${code}`);
})

child9.stdout.on('data', (data)=> {
   console.log(`simulation_random_480-540.py: \n${data}`)
});
child9.stderr.on('data', (data)=> {
   console.log(`simulation_random_480-540.py: \n${data}`)
});
child9.on('close', (code) => {
   console.log(`simulation_random_480-540.py exited with code ${code}`);
})

child10.stdout.on('data', (data)=> {
   console.log(`simulation_random_540-600.py: \n${data}`)
});
child10.stderr.on('data', (data)=> {
   console.log(`simulation_random_540-600.py: \n${data}`)
});
child10.on('close', (code) => {
   console.log(`simulation_random_540-600.py exited with code ${code}`);
})

child11.stdout.on('data', (data)=> {
   console.log(`simulation_random_600-660.py: \n${data}`)
});
child11.stderr.on('data', (data)=> {
   console.log(`simulation_random_600-660.py: \n${data}`)
});
child11.on('close', (code) => {
   console.log(`simulation_random_600-660.py exited with code ${code}`);
})

child12.stdout.on('data', (data)=> {
   console.log(`simulation_random_660-720.py: \n${data}`)
});
child12.stderr.on('data', (data)=> {
   console.log(`simulation_random_660-720.py: \n${data}`)
});
child12.on('close', (code) => {
   console.log(`simulation_random_660-720.py exited with code ${code}`);
})

child13.stdout.on('data', (data)=> {
   console.log(`simulation_random_720-780.py: \n${data}`)
});
child13.stderr.on('data', (data)=> {
   console.log(`simulation_random_720-780.py: \n${data}`)
});
child13.on('close', (code) => {
   console.log(`simulation_random_720-780.py exited with code ${code}`);
})

child14.stdout.on('data', (data)=> {
   console.log(`simulation_random_780-840.py: \n${data}`)
});
child14.stderr.on('data', (data)=> {
   console.log(`simulation_random_780-840.py: \n${data}`)
});
child14.on('close', (code) => {
   console.log(`simulation_random_780-840.py exited with code ${code}`);
})

child15.stdout.on('data', (data)=> {
   console.log(`simulation_random_840-900.py: \n${data}`)
});
child15.stderr.on('data', (data)=> {
   console.log(`simulation_random_840-900.py: \n${data}`)
});
child15.on('close', (code) => {
   console.log(`simulation_random_840-900.py exited with code ${code}`);
})

child16.stdout.on('data', (data)=> {
   console.log(`simulation_random_900-960.py: \n${data}`)
});
child16.stderr.on('data', (data)=> {
   console.log(`simulation_random_900-960.py: \n${data}`)
});
child16.on('close', (code) => {
   console.log(`simulation_random_900-960.py exited with code ${code}`);
})

child17.stdout.on('data', (data)=> {
   console.log(`simulation_random_960-1001.py: \n${data}`)
});
child17.stderr.on('data', (data)=> {
   console.log(`simulation_random_960-1001.py: \n${data}`)
});
child17.on('close', (code) => {
   console.log(`simulation_random_960-1001.py exited with code ${code}`);
})

