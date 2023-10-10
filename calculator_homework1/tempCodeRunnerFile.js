<script>
//Calculation result
function clearResult() { //Clear interface
    document.getElementById("result").value = ''; 
} //Gets a reference to an HTML element. Use JS built-in libraries to achieve computing functions, and so on
 
function deleteLastChar() { //Delete a character
    let result = document.getElementById("result").value;
    document.getElementById("result").value = result.slice(0, -1);
}
 
function appendChar(char) {
    let result = document.getElementById("result").value;
    document.getElementById("result").value = result + char;
}
 
function calculateResult() {
    let result = document.getElementById("result").value;
    let calculatedResult = eval(result);
    document.getElementById("result").value = calculatedResult;
}
 
function calculateSquare() {
    let result = document.getElementById("result").value;
    let calculatedResult = eval(result) ** 2;
    document.getElementById("result").value = calculatedResult;
}
 
function calculateSquareRoot() {
    let result = document.getElementById("result").value;
    let calculatedResult = Math.sqrt(eval(result));
    document.getElementById("result").value = calculatedResult;
}
 
 
function calculateCos() {
  try {
    result.value = Math.cos(eval(result.value));
  } catch (error) {
    result.value = 'ERROR';
  }
}
 
function calculateSin() {
  try {
    result.value = Math.sin(eval(result.value));
  } catch (error) {
    result.value = 'ERROR';
  }
}
</script>