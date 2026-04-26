// Prompt Lab: Tune Your Creativity & Control

// Function to simulate AI response based on temperature
function generateResponse(instruction, temperature) {
    let response = "";

    if (temperature < 0.3) {
        response = "This is a precise and structured response based strictly on the instruction.";
    } else if (temperature < 0.7) {
        response = "This response is balanced, with some creativity but still follows the instruction clearly.";
    } else {
        response = "This is a highly creative and imaginative response that expands beyond the basic instruction!";
    }

    return `
Instruction: ${instruction}
Temperature: ${temperature}

AI Response:
${response}
-----------------------------------
`;
}

// Different instruction-based prompts
const instruction1 = "Explain the importance of studying for exams.";
const instruction2 = "Write a short story about a student preparing for exams.";
const instruction3 = "Create a funny and imaginative story about exams.";

// Testing different temperature values
console.log(generateResponse(instruction1, 0.2));
console.log(generateResponse(instruction2, 0.5));
console.log(generateResponse(instruction3, 0.9));