(() => {
  // retrieving and parsing expected answer
  const expAns = sessionStorage.getItem("card::expectedAnswer")?.trim() || "";

  // retrieving typed answer
  const typeAns = sessionStorage.getItem("card::typedAnswer")?.trim() || "";

  function htmlEscape(string) {
    return string.replaceAll('&', '&amp;')
                 .replaceAll('<', '&lt;')
                 .replaceAll('>', '&gt;')
                 .replaceAll("'", '&#39;')
                 .replaceAll('"', '&quot;');
  }

  function stringDiff2(s1, s2) {
    const n = s1.length;
    const m = s2.length;

    // Matrix of common subsequences' lengths
    const M = Array.from({length: n + 1}, () => Array(m + 1).fill(0)); // init
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < m; j++) {
        if (s1[i] === s2[j]) {
          M[i+1][j+1] = M[i][j] + 1;
        }
      }
    }

    // longest common subsequence in a given minor of M
    function minorLCS( [n1, n2], [m1, m2] ) {
      let max = 0;
      let pos;
      for (let i = n1; i <= n2; i++) {
        for (let j = m1; j <= m2; j++) {
          const Mij = Math.min(M[i][j], j - m1 + 1, i - n1 + 1);
          if (Mij > max) {
            max = Mij;
            pos = [i, j];
          }
        }
      }
      return { "length": max, pos };
    }

    // Ratcliff-Obershelp implementation  
    function Diff2( [n1, n2], [m1, m2] ) {
      const LCS = minorLCS( [n1, n2], [m1, m2] );
      const length0 = LCS.length;
      
      if (length0 === 0) { // purely different part (base case)
        let diffTyped = s1.substring(n1 - 1, n2);
        let diffExpected = s2.substring(m1 - 1, m2);
        if (diffTyped) {
          diffTyped = '<span class="typeBad">' + htmlEscape(diffTyped) + '</span>';
        } else if (diffExpected) {
          diffTyped = '<span class="typeMissed">' + "-".repeat(diffExpected.length) + '</span>';
        }
        if (diffExpected) {
          diffExpected = '<span class="typeMissed">' + htmlEscape(diffExpected) + '</span>';
        }
        return {
          diffTyped,
          diffExpected
        };
      } else { // recursive case
        const [n0, m0] = LCS.pos;
        const D1 = Diff2( [n1, n0-length0], [m1, m0-length0] ); // recursive calls
        const D2 = Diff2( [n0+1, n2], [m0+1, m2] );
        const diffCommon = '<span class="typeGood">' + htmlEscape(s1.substring(n0 - length0, n0)) + '</span>'; // common part
        return {
          diffTyped: D1.diffTyped + diffCommon + D2.diffTyped,
          diffExpected: D1.diffExpected + diffCommon + D2.diffExpected
        }
      }
    }

    return Diff2([1, n], [1, m]); // full diff
  }

  // displaying the diff
  const typeAnsL = document.getElementById('typeans');
  if (typeAns) {
    const ansDiff = stringDiff2(typeAns, expAns);
    typeAnsL.outerHTML = '<code id="typeans">' + 
                         ansDiff.diffTyped +
                         '<br><span id="typearrow">↓</span><br>' +
                         ansDiff.diffExpected +         
                         '</code>';
  } else { // (no answer typed)
    typeAnsL.outerHTML = '<code id="typeans">' + expAns + '</code>';
  }
})();