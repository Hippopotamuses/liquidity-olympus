const { spawn } = require('child_process');

const child1 = spawn('python3', ["./simulation_variables_a.py"]);
const child2 = spawn('python3', ["./simulation_variables_b.py"]);
const child3 = spawn('python3', ["./simulation_variables_c.py"]);
const child4 = spawn('python3', ["./simulation_variables_d.py"]);
const child5 = spawn('python3', ["./simulation_variables_e.py"]);
const child6 = spawn('python3', ["./simulation_variables_f.py"]);
const child7 = spawn('python3', ["./simulation_variables_g.py"]);
const child8 = spawn('python3', ["./simulation_variables_h.py"]);

child1.stdout.on('data', (data)=> {
    console.log(`simulation_variables_a.py: \n${data}`)
});
child1.stderr.on('data', (data)=> {
    console.log(`simulation_variables_a.py: \n${data}`)
});
child1.on('close', (code) => {
    console.log(`simulation_variables_a.py exited with code ${code}`);
})

child2.stdout.on('data', (data)=> {
    console.log(`simulation_variables_b.py: \n${data}`)
});
child2.stderr.on('data', (data)=> {
    console.log(`simulation_variables_b.py: \n${data}`)
});
child2.on('close', (code) => {
    console.log(`simulation_variables_b.py exited with code ${code}`);
})

child3.stdout.on('data', (data)=> {
    console.log(`simulation_variables_c.py: \n${data}`)
});
child3.stderr.on('data', (data)=> {
    console.log(`simulation_variables_c.py: \n${data}`)
});
child3.on('close', (code) => {
    console.log(`simulation_variables_c.py exited with code ${code}`);
})

child4.stdout.on('data', (data)=> {
    console.log(`simulation_variables_d.py: \n${data}`)
});
child4.stderr.on('data', (data)=> {
    console.log(`simulation_variables_d.py: \n${data}`)
});
child4.on('close', (code) => {
    console.log(`simulation_variables_d.py exited with code ${code}`);
})

child5.stdout.on('data', (data)=> {
    console.log(`simulation_variables_e.py: \n${data}`)
});
child5.stderr.on('data', (data)=> {
    console.log(`simulation_variables_e.py: \n${data}`)
});
child5.on('close', (code) => {
    console.log(`simulation_variables_e.py exited with code ${code}`);
})

child6.stdout.on('data', (data)=> {
    console.log(`simulation_variables_f.py: \n${data}`)
});
child6.stderr.on('data', (data)=> {
    console.log(`simulation_variables_f.py: \n${data}`)
});
child6.on('close', (code) => {
    console.log(`simulation_variables_f.py exited with code ${code}`);
})

child7.stdout.on('data', (data)=> {
    console.log(`simulation_variables_g.py: \n${data}`)
});
child7.stderr.on('data', (data)=> {
    console.log(`simulation_variables_g.py: \n${data}`)
});
child7.on('close', (code) => {
    console.log(`simulation_variables_g.py exited with code ${code}`);
})

child8.stdout.on('data', (data)=> {
    console.log(`simulation_variables_h.py: \n${data}`)
});
child8.stderr.on('data', (data)=> {
    console.log(`simulation_variables_h.py: \n${data}`)
});
child8.on('close', (code) => {
    console.log(`simulation_variables_h.py exited with code ${code}`);
})