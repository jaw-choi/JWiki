참고 : https://wn42.tistory.com/111

비멤버함수에 대해서 -> 즉 클래스 밖에 선언해도 되는 함수는 비멤버함수임
즉, 클래스의 변수를 안쓰는 함수는 비멤버 함수임
즉 매개변수로 클래스를 받아서 other.x처럼 쓰는건 비멤버함수
이때(operator 오버로딩 할 때)는 변수가 public이든 상관없이 쓴다.

x + other.x 쓰는것은 x쓰기 때문에 멤버함수

friend + 비멤버함수

frined와 singleton

싱글톤의 인스턴스 static변수는 private으로 둔다.
Engine() 생성자에서 instance = this;
//Lazy Init도 가능(쓰기 직전 생성) - 그러나 우린 바로 생성한다.


