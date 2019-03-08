package org.tektutor;

import static org.junit.Assert.*;
import org.junit.Test;

public class AppTest {


	@Test
	public void testSayHello() {

		App app = new App();

		String expectedResponse = "Hello DevOps!";
		String actualResponse   = app.sayHello();

		assertEquals ( expectedResponse, actualResponse );

	}

}
