<div style = "font-family: times; font-size: 18px">
    <div>
        <h1 style = "font-size: 40px"> 
            241. Different Ways to Add Parentheses
        </h1>
    </div>
    <div style = "margin: 20px">
        <div>
            <b> Type: </b>
            <span style = "color: blue"> Medium </span>
        </div>
        <div>
            <b> Topics: </b>
            <span> Math, String, Dynamic Programming, Recursion, Memoization </span>
        </div>
        <div>
            <b> Companies: </b>
            <span> Amazon, Bloomberg, Google, Adobe, Salesforce </span>
        </div>
    </div><hr>
    <div>
        <p>
            Given a string <code style = "font-family: times">expression</code> of numbers and operators, return <i>all possible results from computing all the different possible ways to group numbers and operators</i>. You may return the answer in <b>any order</b>.
        </p>
        <p>
            The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed <code style = "font-family: times">10<sup>4</sup></code>.
        </p>
    </div><hr>
    <div>
        <div>
            <b> Example 1:</b>
            <div style = "margin: 20px">
                <b>Input:</b> expression = "2-1-1" <br>
                <b>Output:</b> [0,2] <br>
                <b>Explanation:</b> <br>
                ((2-1)-1) = 0 <br>
                (2-(1-1)) = 2
            </div>
        </div>
        <div>
            <b> Example 2:</b>
            <div style = "margin: 20px">
                <b>Input:</b> expression = "2*3-4*5" <br>
                <b>Output:</b> [-34,-14,-10,-10,10] <br>
                <b>Explanation:</b> <br>
                (2*(3-(4*5))) = -34 <br>
                ((2*3)-(4*5)) = -14 <br>
                ((2*(3-4))*5) = -10 <br>
                (2*((3-4)*5)) = -10 <br>
                (((2*3)-4)*5) = 10
            </div>
        </div>
    </div><hr>
    <div>
        <b> Constraints: </b>
        <ul>
            <li>
                <code style = "font-family: times">1 <= expression.length <= 20 </code>
            </li>
            <li>
                <code style = "font-family: times">expression</code> consists of digits and the operator <code style = "font-family: times">'+'</code>, <code style = "font-family: times">'-'</code>, and <code style = "font-family: times">'*'</code>.
            </li>
            <li>
                All the integer values in the input expression are in the range <code style = "font-family: times">[0, 99]</code>.
            </li>
        </ul>
    </div><hr>
</div>