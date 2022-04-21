class TestClassKt {
    var numberMatrix = Array(10) { mutableSetOf<String>() }

    fun isValid(): Boolean {
        numberMatrix.forEach { set ->
            set.forEach { pn ->
                for (i in 0..pn.length-2) {
                    val pfx = pn.slice(0..i)
                    if (pfx in numberMatrix[pfx.length - 1]) {
                        return false
                    }
                }
            }
        }
        return true
    }

    fun test() {
        val t = readLine()!!.toInt() - 1

        for (i in 0..t) {
            val n = readLine()!!.toInt() - 1
            for (j in 0..n) {
                val number = readLine()!!
                numberMatrix[number.length - 1].add(number)
            }
            if (isValid()) {
                println("YES")
            } else {
                println("NO")
            }
            numberMatrix = Array(10) { mutableSetOf<String>() }
        }
    }

    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            TestClassKt().test()
        }
    }


}

