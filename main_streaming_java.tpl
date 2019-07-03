		/*
		 * {{NAME}}
		 */
		if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_enabled)))
		{
			ArrayList<CurrencyPair> {{Name}}_cp = ep.getExchange(Exchanges.{{NAME}}).getCurrencyPairs();
			//Create a ticker from {{name}}
			if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_ticker_enabled)))
			{
				thds.addAll(ExchangesFactory.get{{Name}}Factory().create_ticker_feeders(ep, ctx, {{Name}}_cp));
			}
			// BUG : orderbook and tickers should be requested on the same thread or they are mutually exclusive
			//Create a orderbook from {{name}}
			if (Boolean.parseBoolean(Config.getInstance().get(Constants.{{name}}_orderbook_enabled)))
			{
				thds.addAll(ExchangesFactory.get{{Name}}Factory().create_orderbook_feeders(ep, ctx, {{Name}}_cp));
			}
		}

